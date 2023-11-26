import boto3
import time

def lambda_handler(event, context):
    cloudfront_distribution_id = 'E7BY6YBTMK4Y5'
    paths = ['/*']

    cloudfront_client = boto3.client('cloudfront')

    # Create a CloudFront invalidation
    response = cloudfront_client.create_invalidation(
        DistributionId=cloudfront_distribution_id,
        InvalidationBatch={
            'Paths': {
                'Quantity': len(paths),
                'Items': paths
            },
            'CallerReference': str(int(time.time()))
        }
    )

    print(response)
