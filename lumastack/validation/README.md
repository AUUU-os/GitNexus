# LumaStack v3 Validation

Status: scaffold validation layer, not verified from LumaStack_v2.zip.

## Purpose

This folder defines the validation checklist for the generated LumaStack v3 scaffold.

## Required Validation Areas

- Root artifact manifest exists and keeps verifiedFromZip false.
- SYSTEM_STATE.json exists and records current scaffold policy.
- Module contracts exist and declare guards.
- Agent contracts exist and deny unsafe actions by default.
- Pipeline contracts exist and declare rollback for write steps.
- Documentation exists for major layers.
- Drive artifact metadata remains consistent.

## Pass Rules

- Required checks must pass.
- No external autonomy claims.
- No ZIP verification claims without inspected source material.
- No delete, force push, or public sharing changes without explicit approval.

## Next

- RUN validation checklist
- CREATE release snapshot
- TRACE releaseSnapshotPipeline

AUUU
