import json  
import boto3  
import pandas as pd  
from io import StringIO  

def lambda_handler(event, context):  
    s3 = boto3.client('s3')  
    comprehend = boto3.client('comprehend')  

    try:  
        bucket = event['Records'][0]['s3']['bucket']['name']  
        key = event['Records'][0]['s3']['object']['key']  
        
        response = s3.get_object(Bucket=bucket, Key=key)  
        data = response['Body'].read().decode('utf-8')  
        
        df = pd.read_csv(StringIO(data))  

        if 'review_description' not in df.columns:  
            return {  
                'statusCode': 400,  
                'body': json.dumps("Column 'review_description' not found.")  
            }  


        sample_df = df.sample(n=25000, random_state=1)  

        sentiments = []  
        for review in sample_df['review_description']:  
            sentiment = comprehend.detect_sentiment(Text=review, LanguageCode='en')  
            sentiments.append(sentiment['Sentiment'])  

        sample_df['Sentiment'] = sentiments  
         
        output_key = 'output/' + key.split('/')[-1] 
        output_csv = sample_df.to_csv(index=False)  
        

        s3.put_object(Bucket=bucket, Key=output_key, Body=output_csv)  

        return {  
            'statusCode': 200,  
            'body': json.dumps('Sentiment analysis completed successfully!')  
        }  

    except Exception as e:  
        print(f"Error: {str(e)}")   
        return {  
            'statusCode': 500,  
            'body': json.dumps(f"Error processing file: {str(e)}")  
        }