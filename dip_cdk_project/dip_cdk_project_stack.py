from aws_cdk import(aws_s3 as _s3,
    core 
    ) 

class DipCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _s3.Bucket(
            self,
            "myBucketID",
            bucket_name="myfirstcdkprojectbkt1004",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )

        mybucket=_s3.Bucket(self, "myBucketId1")
        print(mybucket.bucket_name)
        output_1=core.CfnOutput(self,"myBucketOutput1",value=mybucket.bucket_name,description=f"My first cdk bucket",export_name="myBucketOutput1")
        
