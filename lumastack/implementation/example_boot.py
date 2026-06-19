"""Example boot for LumaStack v3 implementation skeleton."""

from lumastack_runtime import create_runtime


def main() -> None:
    runtime = create_runtime()
    command_result = runtime.run_command_pipeline("TRACE releaseSnapshotPipeline")
    trace_result = runtime.trace_release_snapshot_pipeline()

    print("commandRoute=", command_result["classification"]["route"])
    print("traceStatus=", trace_result["status"])
    print("omegaSignal=", trace_result["omegaSignal"])


if __name__ == "__main__":
    main()
