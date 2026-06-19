# LumaStack v3 Agent Contracts

Status: scaffold contracts, not verified from LumaStack_v2.zip.

## Purpose

This file set defines the first stable contract layer for LumaStack v3 agents.

## Agent Rules

- Every agent must bind to a module contract.
- Every agent must declare receives and returns.
- State effects must be explicit.
- Agents cannot claim external autonomy.
- Agents cannot claim ZIP verification without inspected source material.
- External writes, merge, public share, delete, and force push require explicit approval.

## Current Agents

- lumaParserAgent
- lumaProcessorAgent
- lumaLinkerAgent
- lumaClassifierAgent
- lumaRegistryAgent
- lumaPipelineAgent
- omegaHowlAgent

## Next

- CREATE pipeline contracts
- CREATE validation checklist
- CREATE release snapshot

AUUU
