import argparse
import yaml, json
import os
from alectio_sdk.flask_wrapper import Pipeline
from process import train, test, infer, getdatasetstate
import logging

# parser = argparse.ArgumentParser()
# parser.add_argument("--config", help="Path to config.yaml", required=True)
# args = parser.parse_args()

with open("./config.yaml", "r") as stream:
    args = yaml.safe_load(stream)

AlectioPipeline = Pipeline(
    name=args["exp_name"],
    train_fn=train,
    test_fn=test,
    infer_fn=infer,
    getstate_fn=getdatasetstate,
    args=args,
    token="hPrjnEpRi0jLikGNNU8lIiCulCbdHAMJeIcBOc2XB4",
)

app = AlectioPipeline.app
