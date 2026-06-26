# this file was auto-generated!


from openminds.latest.controlled_terms.dependency_impact import DependencyImpact


DependencyImpact.complete_outage = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/completeOutage",
    definition="A thing becomes entirely nonfunctional if the thing it depends on is unavailable.",
    name="complete outage",
)

DependencyImpact.critical_function_loss = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/criticalFunctionLoss",
    definition="Essential or mission-critical features of a thing stop working if the thing it depends on is unavailable.",
    name="critical function loss",
)

DependencyImpact.data_staleness = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/dataStaleness",
    definition="A thing must rely on cached or outdated data because fresh data cannot be retrieved if the thing it depends on is unavailable.",
    name="data staleness",
)

DependencyImpact.data_unavailability = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/dataUnavailability",
    definition="A thing cannot retrieve any required data, causing operations to halt or fail, if the thing it depends on is unavailable.",
    name="data unavailability",
)

DependencyImpact.error_propagation = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/errorPropagation",
    definition="A thing emits errors that surface to users or downstream systems if the thing it depends on is unavailable.",
    name="error propagation",
)

DependencyImpact.fallback_mode_activation = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/fallbackModeActivation",
    definition="A thing switches to an intentionally designed degraded or alternate operating mode if the thing it depends on is unavailable.",
    name="fallback mode activation",
)

DependencyImpact.non_critical_function_loss = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/non-criticalFunctionLoss",
    definition="Secondary or optional features of a thing stop working while core functions continue if the thing it depends on is unavailable.",
    name="non-critical function loss",
)

DependencyImpact.queue_build_up = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/queueBuild-up",
    definition="Requests or tasks directed to a thing accumulate because normal processing cannot proceed if the thing it depends on is unavailable.",
    name="queue build-up",
)

DependencyImpact.reduced_performance = DependencyImpact(
    id="https://openminds.om-i.org/instances/dependencyImpact/reducedPerformance",
    definition="A thing remains functional but responds more slowly or with higher latency if the thing it depends on is unavailable.",
    name="reduced performance",
)
