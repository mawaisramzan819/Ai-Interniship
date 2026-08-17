"""
Day 11 - Task 1: Data Processing Pipeline
Xeven Solutions AI Engineer Internship

This script processes records using loops, enumerate(), zip(), break, and continue.
"""

def process_data_pipeline() -> dict:
    """Processes 1000 records with validation, transformation, and error handling."""
    # Generate dummy raw records
    user_ids = list(range(1001, 2001))  # 1000 user IDs
    user_names = [f"user_{i}" for i in range(1000)]
    scores = [i * 1.5 if i % 13 != 0 else -1 for i in range(1000)]  # -1 represents corrupted record
    
    # Validation: Ensure data sources have matching lengths
    if not (len(user_ids) == len(user_names) == len(scores)):
        raise ValueError("Data sources have mismatched lengths!")
        
    processed_records = []
    skipped_count = 0
    total_records = len(user_ids)
    
    print("=" * 50)
    print("=== STARTING DATA PROCESSING PIPELINE (1000 RECORDS) ===")
    print("=" * 50)
    
    # Combine data sources using zip() and track index using enumerate()
    for index, (u_id, name, score) in enumerate(zip(user_ids, user_names, scores), start=1):
        
        # 1. Skip invalid/corrupted records using 'continue'
        if score < 0:
            skipped_count += 1
            continue
            
        # 2. Critical error check: stop processing if corrupted system ID encountered
        if u_id == 1999:
            print(f"[ALERT] Critical System Alert at Record #{index}: Emergency Stop triggered!")
            break
            
        # 3. Transform data
        transformed_record = {
            "id": u_id,
            "username": name.upper(),
            "score": round(score, 2),
            "status": "PASSED" if score >= 50 else "FAILED"
        }
        processed_records.append(transformed_record)
        
        # Print progress checkpoint every 200 records
        if index % 200 == 0:
            print(f"Progress: Record #{index} of {total_records} processed successfully.")
            
    summary = {
        "total_input": total_records,
        "successfully_processed": len(processed_records),
        "skipped_invalid": skipped_count,
    }
    
    print("\n--- PIPELINE SUMMARY ---")
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print()
    
    return summary


if __name__ == "__main__":
    process_data_pipeline()
