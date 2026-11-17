# openIMIS Backend calcrule_social_protection reference module
# description
This calculation will calculate amount of payment for beneficiary based on whether they meet criteria specified in custom filters of payment plan.

## Bills

Each beneficiary (or group beneficiary) paid by a payment plan gets a bill whose subject and single line are the
beneficiary. The bill's terms are `<benefit plan code>-<payment cycle end date>: <beneficiary id>` and the line's
code is the beneficiary id: a bill carries no person name or group code.

A payment above the payment plan's limit per single transaction is not billed at once: the bill and benefit are held
in a task (source `calcrule_social_protection`) whose data is the string form of a Python dict. Completing the task
creates the bill as validated, failing it creates the bill as cancelled, whatever characters the held values contain.

A benefit plan without an end date is billed like any other: the bill, its line and the benefit carry no end of
validity.
