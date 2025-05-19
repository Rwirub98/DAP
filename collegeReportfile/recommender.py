import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class CourseRecommender:
    def __init__(self, df):
        """
        Initialize the recommender with course data
        
        Args:
            df (pd.DataFrame): Loaded and cleaned DataFrame
        """
        self.df = df.copy()
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.cosine_sim = None
        self._prepare_data()
    
    def _prepare_data(self):
        """Prepare data for recommendation system"""
        # Fill NaN with empty string
        self.df['Course Name'] = self.df['Course Name'].fillna('')
        self.df['Description'] = self.df['Course Name'] + ' ' + self.df['Learning Product Type']
        
        # TF-IDF matrix
        tfidf_matrix = self.tfidf.fit_transform(self.df['Description'])
        
        # Cosine similarity matrix
        self.cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    def recommend_courses(self, title, n=5):
        """
        Get course recommendations based on similarity
        
        Args:
            title (str): Course title to find similar courses for
            n (int): Number of recommendations to return
            
        Returns:
            pd.DataFrame: DataFrame with recommended courses
        """
        # Get the index of the course that matches the title
        idx = self.df[self.df['Course Name'].str.contains(title, case=False)].index[0]
        
        # Get pairwise similarity scores
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        
        # Sort courses by similarity score
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Get scores of top n most similar courses (skip the first which is itself)
        sim_scores = sim_scores[1:n+1]
        
        # Get course indices
        course_indices = [i[0] for i in sim_scores]
        
        # Return top n most similar courses
        return self.df.iloc[course_indices][
            ['Course Name', 'Course Provided By', 'Course Rating', 'Course Difficulty']
        ]

if __name__ == "__main__":
    from data_loader import load_coursera_data
    df = load_coursera_data("coursera-courses-overview.csv")
    
    recommender = CourseRecommender(df)
    
    # Example recommendation
    print("\nRecommendations for 'Data Science':")
    print(recommender.recommend_courses("Data Science"))
    
    print("\nRecommendations for 'Machine Learning':")
    print(recommender.recommend_courses("Machine Learning"))