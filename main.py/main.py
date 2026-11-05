from src.data_ingestion import data_ingestion
def main():
    
    df = data_ingestion()
    print(df.head())
    
main()    