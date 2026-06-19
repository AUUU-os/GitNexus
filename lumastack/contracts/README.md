# LumaStack v3 Module Contracts

Status: scaffold contracts, not verified from LumaStack_v2.zip.

## Purpose

This folder defines the first stable contract layer for LumaStack v3 modules.

## Contract Rules

- Use camelCase keys.
- Every module must declare inputs and outputs.
- Side effects must be explicit.
- Delete, force push, and public sharing changes are disallowed by default.
- verifiedFromZip remains false until a real source ZIP or source repository is inspected.

## Current Modules

- parser
- processor
- linker
- classifier
- registry
- capsuleMemory
- apiInterpreter
- cliInterface

## Next

- CREATE agent contracts
- CREATE pipeline contracts
- CREATE validation checklist
- CREATE release snapshot

AUUU
