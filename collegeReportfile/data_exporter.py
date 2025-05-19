import pandas as pd
import json

def export_analysis_results(df, stats, output_dir='output'):
    """
    Export analysis results to various formats
    
    Args:
        df (pd.DataFrame): Loaded and cleaned DataFrame
        stats (dict): Statistics from exploratory analysis
        output_dir (str): Directory to save output files
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Export cleaned data to CSV
    df.to_csv(f'{output_dir}/cleaned_courses.csv', index=False)
    
    # 2. Export statistics to JSON
    with open(f'{output_dir}/course_statistics.json', 'w') as f:
        json.dump(stats, f, indent=2)
    
    # 3. Export top courses by rating
    top_rated = df.sort_values('Course Rating', ascending=False).head(20)
    top_rated.to_csv(f'{output_dir}/top_rated_courses.csv', index=False)
    
    # 4. Export popular courses by enrollment
    popular = df.sort_values('Enrolled Student Count', ascending=False).head(20)
    popular.to_csv(f'{output_dir}/most_popular_courses.csv', index=False)
    
    print(f"Data exported to {output_dir} directory")

if __name__ == "__main__":
    from data_loader import load_coursera_data
    from exploratory_analysis import perform_eda
    
    df = load_coursera_data("coursera-courses-overview.csv")
    stats = perform_eda(df)
    
    export_analysis_results(df, stats)