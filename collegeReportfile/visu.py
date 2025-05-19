import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_course_distributions(df):
    """
    Create visualizations for Coursera courses data
    
    Args:
        df (pd.DataFrame): Loaded and cleaned DataFrame
    """
    plt.figure(figsize=(15, 10))
    
    # Set style
    sns.set_style("whitegrid")
    
    # 1. Difficulty Distribution
    plt.subplot(2, 2, 1)
    difficulty_counts = df['Course Difficulty'].value_counts()
    sns.barplot(x=difficulty_counts.index, y=difficulty_counts.values)
    plt.title('Course Difficulty Distribution')
    plt.xticks(rotation=45)
    
    # 2. Product Type Distribution
    plt.subplot(2, 2, 2)
    product_counts = df['Learning Product Type'].value_counts()
    sns.barplot(x=product_counts.index, y=product_counts.values)
    plt.title('Learning Product Type Distribution')
    plt.xticks(rotation=45)
    
    # 3. Rating Distribution
    plt.subplot(2, 2, 3)
    sns.histplot(df['Course Rating'].dropna(), bins=20, kde=True)
    plt.title('Course Rating Distribution')
    
    # 4. Enrollment Distribution (log scale)
    plt.subplot(2, 2, 4)
    sns.histplot(df['Enrolled Student Count'].dropna(), bins=20, kde=True, log_scale=True)
    plt.title('Enrollment Distribution (Log Scale)')
    
    plt.tight_layout()
    plt.savefig('course_distributions.png')
    plt.close()

def plot_top_providers(df, n=10):
    """
    Plot top providers by number of courses
    
    Args:
        df (pd.DataFrame): Loaded and cleaned DataFrame
        n (int): Number of top providers to show
    """
    plt.figure(figsize=(12, 6))
    top_providers = df['Course Provided By'].value_counts().head(n)
    sns.barplot(x=top_providers.values, y=top_providers.index)
    plt.title(f'Top {n} Course Providers by Number of Courses')
    plt.xlabel('Number of Courses')
    plt.tight_layout()
    plt.savefig('top_providers.png')
    plt.close()

if __name__ == "__main__":
    from data_loader import load_coursera_data
    df = load_coursera_data("coursera-courses-overview.csv")
    
    plot_course_distributions(df)
    plot_top_providers(df)
    
    print("Visualizations saved as 'course_distributions.png' and 'top_providers.png'")