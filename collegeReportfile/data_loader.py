import pandas as pd

def load_coursera_data(filepath):
    """
    Load and clean the Coursera courses dataset
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Cleaned DataFrame with proper data types
    """
    # Load the data
    df = pd.read_csv(filepath)
    
    # Clean 'Enrolled Student Count' column
    df['Enrolled Student Count'] = df['Enrolled Student Count'].replace('Missing', pd.NA)
    df['Enrolled Student Count'] = df['Enrolled Student Count'].str.replace('k', '000')
    df['Enrolled Student Count'] = df['Enrolled Student Count'].str.replace('m', '000000')
    df['Enrolled Student Count'] = pd.to_numeric(df['Enrolled Student Count'], errors='coerce')
    
    # Clean 'Course Rated By' column
    df['Course Rated By'] = pd.to_numeric(df['Course Rated By'], errors='coerce')
    
    # Clean 'Course Rating' column
    df['Course Rating'] = pd.to_numeric(df['Course Rating'], errors='coerce')
    
    # Extract organization from 'Course Provided By'
    df['Organization'] = df['Course Provided By'].str.split(',').str[0]
    
    return df

if __name__ == "__main__":
    # Example usage
    df = load_coursera_data("coursera-courses-overview.csv")
    print(df.head())
    print(f"\nDataset contains {len(df)} courses")