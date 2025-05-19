import pandas as pd
from collections import Counter

def perform_eda(df):
    """
    Perform exploratory data analysis on Coursera courses data
    
    Args:
        df (pd.DataFrame): Loaded and cleaned DataFrame
        
    Returns:
        dict: Dictionary containing key statistics
    """
    results = {}
    
    # Basic statistics
    results['total_courses'] = len(df)
    results['unique_providers'] = df['Course Provided By'].nunique()
    results['unique_orgs'] = df['Organization'].nunique()
    
    # Difficulty distribution
    results['difficulty_dist'] = dict(Counter(df['Course Difficulty']))
    
    # Product type distribution
    results['product_type_dist'] = dict(Counter(df['Learning Product Type']))
    
    # Rating statistics
    results['avg_rating'] = df['Course Rating'].mean()
    results['median_rating'] = df['Course Rating'].median()
    
    # Enrollment statistics
    results['avg_enrollment'] = df['Enrolled Student Count'].mean()
    results['median_enrollment'] = df['Enrolled Student Count'].median()
    
    # Top providers by course count
    results['top_providers'] = df['Course Provided By'].value_counts().head(10).to_dict()
    
    # Top rated courses
    top_rated = df.sort_values('Course Rating', ascending=False).head(5)[
        ['Course Name', 'Course Provided By', 'Course Rating']
    ].to_dict('records')
    results['top_rated_courses'] = top_rated
    
    # Most popular courses by enrollment
    popular = df.sort_values('Enrolled Student Count', ascending=False).head(5)[
        ['Course Name', 'Course Provided By', 'Enrolled Student Count']
    ].to_dict('records')
    results['most_popular_courses'] = popular
    
    return results

if __name__ == "__main__":
    from data_loader import load_coursera_data
    df = load_coursera_data("coursera-courses-overview.csv")
    stats = perform_eda(df)
    
    print("\nExploratory Data Analysis Results:")
    for key, value in stats.items():
        print(f"\n{key.replace('_', ' ').title()}:")
        print(value)