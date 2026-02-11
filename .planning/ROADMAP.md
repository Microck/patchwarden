# PatchWarden Roadmap

## Overview

Multi-agent security scanner for game mods that detects malware before gamers install them. Built for Microsoft AI Dev Days Hackathon 2026.

**Timeline:** 5 weeks (Feb 10 - Mar 15, 2026)
**Target Prizes:** AI Apps & Agents ($20k), Enterprise ($10k)

---

## Phase 1: Foundation

**Goal:** File upload pipeline + mod type detection

**Duration:** ~1 week

**Requirements Covered:**
- FOUND-01: Foundry project initialized
- FOUND-02: File upload endpoint for mod files
- FOUND-03: Mod extraction and type detection
- FOUND-04: Azure Blob Storage for uploaded mods

**Success Criteria:**
1. Foundry project running
2. File upload endpoint accepts .jar files
3. Mod type (Minecraft) detected correctly
4. Files stored in Azure Blob Storage

**Deliverables:**
- `src/api/upload.py`
- `src/agents/intake_agent.py`
- `src/storage/blob.py`

---

## Phase 2: Static Analysis

**Goal:** Decompilation + pattern matching

**Duration:** ~1 week

**Requirements Covered:**
- STAT-01: Intake Agent extracts .jar mod files
- STAT-02: Static Agent decompiles Java classes
- STAT-03: Static Agent pattern matches suspicious code
- STAT-04: Known malware signature database in Azure AI Search
- STAT-05: Suspicious pattern catalog (obfuscation, network calls, file writes)

**Success Criteria:**
1. .jar files extracted successfully
2. Java classes decompiled to readable source
3. Suspicious patterns detected (obfuscation, network, file I/O)
4. Signature database searchable
5. Catalog of 10+ suspicious patterns defined

**Deliverables:**
- `src/agents/static_agent.py`
- `src/analysis/decompiler.py`
- `src/analysis/patterns.py`
- `data/signatures/`

---

## Phase 3: Behavior Analysis

**Goal:** LLM-based behavior prediction

**Duration:** ~1 week

**Requirements Covered:**
- BEH-01: Behavior Agent analyzes decompiled code with LLM
- BEH-02: Behavior Agent predicts file system access
- BEH-03: Behavior Agent predicts network activity
- BEH-04: Behavior Agent predicts startup/persistence behavior

**Success Criteria:**
1. LLM analyzes code and produces behavior prediction
2. File access predictions accurate (read/write paths)
3. Network activity predictions (URLs, ports)
4. Persistence behavior predictions (startup, registry)

**Deliverables:**
- `src/agents/behavior_agent.py`
- `src/models/behavior.py`

---

## Phase 4: Reputation & Verdict

**Goal:** Author reputation + final verdict synthesis

**Duration:** ~1 week

**Requirements Covered:**
- REP-01: Reputation Agent looks up author history
- REP-02: Reputation Agent checks for community reports
- REP-03: Author age/activity scoring
- VERD-01: Verdict Agent synthesizes all findings
- VERD-02: Risk score (LOW/MEDIUM/HIGH/CRITICAL)
- VERD-03: Human-readable explanation of findings
- VERD-04: Specific suspicious indicators listed

**Success Criteria:**
1. Author history retrieved (account age, other mods)
2. Community reports checked
3. Author score calculated
4. All findings synthesized into verdict
5. Risk score assigned correctly
6. Explanation is clear and actionable
7. Specific indicators listed

**Deliverables:**
- `src/agents/reputation_agent.py`
- `src/agents/verdict_agent.py`
- `src/models/verdict.py`

---

## Phase 5: Demo & Submit

**Goal:** Web UI + polished demo

**Duration:** ~1 week

**Requirements Covered:**
- DEMO-01: Web UI for mod upload
- DEMO-02: Planted malware sample for demo
- DEMO-03: 2-minute video showing malware detection
- DEMO-04: README with example scans

**Success Criteria:**
1. Web UI functional for upload and results
2. Malware sample planted and detectable
3. Video shows full detection flow
4. README includes examples

**Deliverables:**
- `src/ui/` (simple web frontend)
- `demo/malware_sample.jar`
- `demo/video.mp4`
- `README.md`

---

## Coverage Validation

All 24 v1 requirements are mapped:
- Phase 1: FOUND-01 to FOUND-04 (4 requirements)
- Phase 2: STAT-01 to STAT-05 (5 requirements)
- Phase 3: BEH-01 to BEH-04 (4 requirements)
- Phase 4: REP-01 to REP-03, VERD-01 to VERD-04 (7 requirements)
- Phase 5: DEMO-01 to DEMO-04 (4 requirements)

**Total: 24/24 requirements covered (100%)**

---

*Last updated: 2026-02-08*
