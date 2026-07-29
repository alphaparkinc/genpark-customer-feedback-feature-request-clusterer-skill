from client import CustomerFeedbackFeatureRequestClustererClient

def main():
    client = CustomerFeedbackFeatureRequestClustererClient()
    entries = ["We need dark mode!", "Please add CSV export feature", "Dark mode would be awesome"]
    res = client.cluster_feedback(entries)
    print(f"Total Analyzed: {res['total_analyzed']}")
    for c in res["top_feature_clusters"]:
        print(f"  [{c['priority']}] {c['cluster_name']} ({c['request_count']} requests)")

if __name__ == "__main__":
    main()
