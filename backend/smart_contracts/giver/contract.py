import beaker
import pyteal as pt
from algokit_utils import DELETABLE_TEMPLATE_NAME, UPDATABLE_TEMPLATE_NAME

app = beaker.Application("crowdfunding")


@app.update(authorize=beaker.Authorize.only_creator(), bare=True)
def update() -> pt.Expr:
    return pt.Assert(
        pt.Tmpl.Int(UPDATABLE_TEMPLATE_NAME),
        comment="Check app is updatable",
    )


@app.delete(authorize=beaker.Authorize.only_creator(), bare=True)
def delete() -> pt.Expr:
    return pt.Assert(
        pt.Tmpl.Int(DELETABLE_TEMPLATE_NAME),
        comment="Check app is deletable",
    )

# Storage keys
campaigns_key = "campaigns"

# Campaign Creation
@app.update()
def create_campaign(
    title: pt.abi.String,
    description: pt.abi.String,
    goal: pt.abi.Int,
    duration: pt.abi.Int,
    fee_percentage: pt.abi.Int,
) -> pt.Expr:
    # Define campaign details
    campaign_details = {
        "title": title,
        "description": description,
        "goal": goal,
        "duration": duration,
        "fee_percentage": fee_percentage,
        "current_funds": 0,
        "contributors": {},
    }

    # Store campaign details in AppLocal storage
    return pt.Seq(
        pt.App.localPut(pt.Bytes(campaigns_key), pt.Txn.application_id(),
                        campaign_details, app_id=0),
        pt.App.localPut(pt.Bytes(campaigns_key), pt.Txn.application_id(),
                        pt.Txn.sender(), 0,
                        app_id=0),  # Initialize contributor amount to 0
    )

# View All Campaigns
@app.external
def view_all_campaigns() -> pt.Expr:
    return pt.App.localGetAll(pt.Bytes(campaigns_key), app_id=0)

# View Campaign Detail
@app.external
def view_campaign_detail(campaign_id: pt.abi.Int) -> pt.Expr:
    return pt.App.localGet(pt.Bytes(campaigns_key), campaign_id, app_id=0)

# Donate to the Campaign
@app.update()
def donate_to_campaign(amount: pt.abi.Int, campaign_id: pt.abi.Int) -> pt.Expr:
    # Retrieve campaign details
    campaign_details = pt.App.localGet(pt.Bytes(campaigns_key), campaign_id, app_id=0)

    # Check if the campaign is still active
    active_campaign = pt.Now() <= campaign_details["duration"]

    # Contribute funds to the campaign
    return pt.If(
        active_campaign,
        pt.Seq(
            pt.App.localPut(pt.Bytes(campaigns_key), campaign_id,
                            campaign_details["current_funds"] + amount, app_id=0),
            pt.App.localPut(pt.Bytes(campaigns_key), campaign_id, pt.Txn.sender(),
                            campaign_details["contributors"].get(
                                pt.Txn.sender(), 0) + amount,
                            app_id=0),
            pt.Int(1),
        ),
        pt.Err("Campaign has ended"),
    )
