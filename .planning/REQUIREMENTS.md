# Requirements

## v1 Requirements

### Foundation (FOUND)

- [ ] **FOUND-01**: Foundry project initialized
- [ ] **FOUND-02**: File upload endpoint for mod files
- [ ] **FOUND-03**: Mod extraction and type detection
- [ ] **FOUND-04**: Azure Blob Storage for uploaded mods

### Static Analysis (STAT)

- [ ] **STAT-01**: Intake Agent extracts .jar mod files
- [ ] **STAT-02**: Static Agent decompiles Java classes
- [ ] **STAT-03**: Static Agent pattern matches suspicious code
- [ ] **STAT-04**: Known malware signature database in Azure AI Search
- [ ] **STAT-05**: Suspicious pattern catalog (obfuscation, network calls, file writes)

### Behavior Analysis (BEH)

- [ ] **BEH-01**: Behavior Agent analyzes decompiled code with LLM
- [ ] **BEH-02**: Behavior Agent predicts file system access
- [ ] **BEH-03**: Behavior Agent predicts network activity
- [ ] **BEH-04**: Behavior Agent predicts startup/persistence behavior

### Reputation (REP)

- [ ] **REP-01**: Reputation Agent looks up author history
- [ ] **REP-02**: Reputation Agent checks for community reports
- [ ] **REP-03**: Author age/activity scoring

### Verdict (VERD)

- [ ] **VERD-01**: Verdict Agent synthesizes all findings
- [ ] **VERD-02**: Risk score (LOW/MEDIUM/HIGH/CRITICAL)
- [ ] **VERD-03**: Human-readable explanation of findings
- [ ] **VERD-04**: Specific suspicious indicators listed

### Demo (DEMO)

- [ ] **DEMO-01**: Web UI for mod upload
- [ ] **DEMO-02**: Planted malware sample for demo
- [ ] **DEMO-03**: 2-minute video showing malware detection
- [ ] **DEMO-04**: README with example scans

---

## v2 Requirements

### Enhancements

- [ ] Support for GTA V mods (.asi, .dll)
- [ ] Support for Unity mods (.dll)
- [ ] Community reporting integration
- [ ] Browser extension for Steam Workshop

---

## Out of Scope

- **Multiple game platforms** — Minecraft only for MVP
- **Sandbox execution** — prediction only, no execution
- **Real-time Workshop integration** — file upload only
- **Enterprise mod management** — consumer focus
- **False positive learning** — static rules only

---

## Traceability

| REQ-ID | Phase | Status | Success Criteria |
|--------|-------|--------|------------------|
| FOUND-01 | Phase 1: Foundation | Pending | Foundry project running |
| FOUND-02 | Phase 1: Foundation | Pending | File upload works |
| FOUND-03 | Phase 1: Foundation | Pending | Mod type detected correctly |
| FOUND-04 | Phase 1: Foundation | Pending | Files stored in Blob Storage |
| STAT-01 | Phase 2: Static | Pending | .jar files extracted |
| STAT-02 | Phase 2: Static | Pending | Java classes decompiled |
| STAT-03 | Phase 2: Static | Pending | Patterns detected |
| STAT-04 | Phase 2: Static | Pending | Signatures searchable |
| STAT-05 | Phase 2: Static | Pending | Catalog of 10+ patterns |
| BEH-01 | Phase 3: Behavior | Pending | LLM analyzes code |
| BEH-02 | Phase 3: Behavior | Pending | File access predicted |
| BEH-03 | Phase 3: Behavior | Pending | Network activity predicted |
| BEH-04 | Phase 3: Behavior | Pending | Persistence predicted |
| REP-01 | Phase 4: Reputation | Pending | Author history retrieved |
| REP-02 | Phase 4: Reputation | Pending | Community reports checked |
| REP-03 | Phase 4: Reputation | Pending | Author score calculated |
| VERD-01 | Phase 4: Reputation | Pending | Findings synthesized |
| VERD-02 | Phase 4: Reputation | Pending | Risk score assigned |
| VERD-03 | Phase 4: Reputation | Pending | Explanation generated |
| VERD-04 | Phase 4: Reputation | Pending | Indicators listed |
| DEMO-01 | Phase 5: Demo | Pending | Web UI functional |
| DEMO-02 | Phase 5: Demo | Pending | Malware sample ready |
| DEMO-03 | Phase 5: Demo | Pending | Video recorded |
| DEMO-04 | Phase 5: Demo | Pending | README complete |

**Coverage:** 24/24 requirements mapped (100%)
