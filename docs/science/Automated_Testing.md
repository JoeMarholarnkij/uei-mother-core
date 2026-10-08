# 🧪 Automated Testing & QA Resonance
**Status:** Integrated (Joe's Brother Mission)
**Domain:** Software Integrity / HIL / Verification

## 1. Unit & Integration Testing (Backend)
Ensuring the logic of the "Nexus Brain" is robust before edge deployment.

### A. C# xUnit Framework
- **Mocks:** Using `Moq` or `NSubstitute` to isolate dependencies (e.g., mocking `IDistributedCache` for Anomaly Detection).
- **In-Memory Testing:** Utilizing `Microsoft.EntityFrameworkCore.InMemory` for rapid database logic validation without hitting Postgres/SQL.
- **Resonance Rule:** Every new service in `SmartPole.Core` must have an accompanying `.Tests` project.

### B. SignalR Hub Testing
- **Protocol:** Testing real-time message delivery and group membership logic using the SignalR Client Hub Connection in a test container.

## 2. Frontend & E2E Testing (React)
Verifying the "Unified Intelligence Console" experience.

### A. Component Testing
- **Tooling:** `Vitest` and `React Testing Library`.
- **Focus:** Validating theme-aware CSS variables and real-time state updates in the `usePoleStore`.

### B. End-to-End (E2E)
- **Tooling:** `Playwright` or `Cypress`.
- **Workflow:** Simulating an SOS alert via the API and asserting that the Dashboard correctly transitions to the "Red Alert" state.

## 3. Hardware-in-the-Loop (HIL) Testing
Critical for **Nexus Air** and **SmartTrolley** hardware integrity.

### A. Jetson/Pico Simulation
- **Edge Mocking:** Creating virtual serial ports and MQTT publishers to simulate LIDAR and sCO2 sensor data.
- **Latency Testing:** Measuring the "Transient Response" time from an Edge sensor trigger to the Dashboard visual update (Target: <200ms).

## 4. Swarm Manifesto: Autonomous Validation
- **Command:** Use the `!{...}` syntax to auto-run tests after every edit.
- **Pipeline:** Integration with GitHub Actions for automated regression testing on every push.
