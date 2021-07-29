from aws_cdk import core, aws_s3, aws_iam


class SPPSAccessS3Stack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        trusted_account = self.node.try_get_context("trusted_account")

        _role_ro = aws_iam.Role(
            self,
            "PTV-SPPS-Support_RO",
            assumed_by=aws_iam.AccountPrincipal(trusted_account),
            role_name="PTV-SPPS-Support_RO",
            description="PTV IDP Cross Account Access to allow R/O Access to all services",
        )

        _role_ro.add_managed_policy(
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("ReadOnlyAccess")
        )

        _role_rw = aws_iam.Role(
            self,
            "PTV-SPPS-Support_RW",
            assumed_by=aws_iam.AccountPrincipal(trusted_account),
            role_name="PTV-SPPS-Support_RW",
            description="PTV IDP Cross Account Access to allow R/O Access to all services",
        )

        _role_rw.add_managed_policy(
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("ReadOnlyAccess")
        )

        _role_rw.add_managed_policy(
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
        )
