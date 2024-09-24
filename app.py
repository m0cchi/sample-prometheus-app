from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_summary import Summary

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info("app_info", "Application info", version="1.0.3")


@app.route("/")
@metrics.summary(
    "requests_by_status",
    "Request latencies by status",
    labels={
        "status": lambda r: r.status_code,
    },
)
@metrics._track(
    Summary,
    lambda metric, time: metric.observe(time),
    metric_kwargs={},
    name="requests_by_status_ex",
    description="ptile",
    labels={
        "status": lambda r: r.status_code,
    },
    initial_value_when_only_static_labels=True,
    registry=metrics.registry,
)
def main():
    return "hello"


@app.route("/skip")
@metrics.do_not_track()
def skip():
    pass  # default metrics are not collected


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
