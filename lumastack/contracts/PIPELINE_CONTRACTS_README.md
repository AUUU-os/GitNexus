# LumaStack v3 Pipeline Contracts

Status: scaffold contracts, not verified from LumaStack_v2.zip.

## Purpose

This folder defines ordered pipeline contracts for safe LumaStack v3 execution traces.

## Pipeline Rules

- Every pipeline must declare inputs, outputs, and ordered steps.
- Every step must declare module, agent, emitted values, and side effects.
- Writes require rollback notes.
- External writes require approval.
- Delete, force push, and public sharing changes are disallowed by default.
- verifiedFromZip remains false until source material is inspected.

## Current Pipelines

- fullBootPipeline
- commandParsePipeline
- apiRequestPipeline
- capsuleSavePipeline
- releaseSnapshotPipeline

## Next

- CREATE validation checklist
- CREATE release snapshot
- TRACE releaseSnapshotPipeline

AUUU
