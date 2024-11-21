# S3 Sentiment Analysis with AWS Lambda and Comprehend

This project provides an AWS Lambda function that automates sentiment analysis for reviews stored in CSV files uploaded to an S3 bucket. The function uses AWS Comprehend to classify the sentiment of reviews and outputs the results back to the S3 bucket for further use.

## Features

- **Automated Workflow**: Triggered by S3 events when a file is uploaded.
- **Sentiment Analysis**: Utilizes AWS Comprehend to detect sentiments (`POSITIVE`, `NEGATIVE`, `NEUTRAL`, `MIXED`).
- **Scalable Sampling**: Processes a sample of up to 25,000 reviews per file for efficient analysis.
- **S3 Output**: Stores the processed CSV file in the `output/` directory of the same S3 bucket.
- **Error Handling**: Provides comprehensive logging and error responses for missing data or unexpected issues.

## Setup and Usage

### Prerequisites

- AWS Lambda with access to:
  - **S3**: Read/write permissions for the bucket.
  - **AWS Comprehend**: To perform sentiment analysis.
- **Python 3.9+**
- Python Libraries:
  - `boto3`
  - `pandas`

### Input File Format

The input CSV file should contain a column named `review_description` with review text. Example:

| review_id | review_description       | rating |
|-----------|--------------------------|--------|
| 1         | "Great app, love it!"    | 5      |
| 2         | "Terrible experience."   | 1      |

### Output File Format

The output CSV file will have an additional `Sentiment` column. Example:

| review_id | review_description       | rating | Sentiment |
|-----------|--------------------------|--------|-----------|
| 1         | "Great app, love it!"    | 5      | POSITIVE  |
| 2         | "Terrible experience."   | 1      | NEGATIVE  |

### Deployment Steps

1. **Set Up S3 Bucket**:
   - Create an S3 bucket.
   - Add an event notification to trigger the Lambda function when a file is uploaded.

2. **Deploy the Lambda Function**:
   - Copy the Python script into an AWS Lambda function.
   - Attach an IAM role with S3 and Comprehend permissions to the Lambda function.

3. **Test the Workflow**:
   - Upload a CSV file to the bucket.
   - Check the `output/` directory for the processed file.

### Configuration

- Adjust the sample size (`n=25000`) in the script to process more or fewer reviews.
- Ensure the `LanguageCode` in AWS Comprehend API calls matches the language of your reviews.

## Notes

- Only English (`LanguageCode='en'`) is supported in this version.
- Reviews are processed sequentially; for high volumes, consider optimizing with batching or multiprocessing.
- The function assumes that uploaded files are CSVs with valid UTF-8 encoding.

## Authors

- **Sanjay M** - [@Sanjay M](https://github.com/sannx4)
- **Thrisheiyan U K** - [@Thrisheiyan U K](https://github.com/ThrisheiyanUK)
- **Ramana V** - [@Ramana V](https://github.com/RamanaVinayak)
- **Nuthalapati.Akash** - [@Nuthalapati.Akash](https://github.com/Akash1660)

---

Feel free to fork, contribute, or open an issue for feedback and suggestions!
