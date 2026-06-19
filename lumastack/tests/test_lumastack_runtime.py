"""Smoke and contract tests for LumaStack v3 implementation skeleton.

These tests validate local runtime behavior only.
They do not perform external writes, GitHub mutations, Drive changes, deletes, or force pushes.
"""

from pathlib import Path
import sys

IMPLEMENTATION_DIR = Path(__file__).resolve().parents[1] / "implementation"
sys.path.insert(0, str(IMPLEMENTATION_DIR))

from lumastack_runtime import Guardrails, LumaRuntime, create_runtime


def test_runtime_imports() -> None:
    runtime = create_runtime()
    assert isinstance(runtime, LumaRuntime)


def test_trace_command_routes_to_cli() -> None:
    runtime = create_runtime()
    result = runtime.run_command_pipeline("TRACE releaseSnapshotPipeline")
    assert result["classification"]["route"] == "cli"
    assert result["classification"]["command"] == "TRACE"
    assert result["plan"]["externalWriteRequired"] is False


def test_release_snapshot_pipeline_trace_passes() -> None:
    runtime = create_runtime()
    trace = runtime.trace_release_snapshot_pipeline()
    assert trace["pipelineId"] == "releaseSnapshotPipeline"
    assert trace["status"] == "passed"
    assert trace["omegaSignal"] == "AUUU"
    assert len(trace["steps"]) == 4
    assert all(step["status"] == "completed" for step in trace["steps"])


def test_guardrails_default_to_safe_values() -> None:
    guardrails = Guardrails()
    assert guardrails.verified_from_zip is False
    assert guardrails.external_autonomy is False
    assert guardrails.may_delete is False
    assert guardrails.may_force_push is False
    assert guardrails.may_change_drive_sharing is False
    assert guardrails.external_writes_require_approval is True


def test_registry_records_command_pipeline_event() -> None:
    runtime = create_runtime()
    assert len(runtime.registry.events) == 0
    runtime.run_command_pipeline("MAP lumastack repository tree")
    assert len(runtime.registry.events) == 1
    assert runtime.registry.events[0]["event"]["type"] == "commandPipeline"


def test_capsule_snapshot_marks_unverified_from_zip() -> None:
    runtime = create_runtime()
    snapshot = runtime.memory.create_snapshot({"state": "test"}, "testSnapshot")
    assert snapshot["snapshotId"] == "testSnapshot"
    assert snapshot["verifiedFromZip"] is False
