from src.tag_system import TAG

def main():
    # Initialize TAG system
    tag = TAG()
    tag.initialize()
    
    try:
        # Add some knowledge chunks
        chunk_id1 = tag.add_knowledge_chunk(
            "GDPR requires explicit consent for processing personal data.",
            domain="Legal"
        )
        
        chunk_id2 = tag.add_knowledge_chunk(
            "Personal data must be processed lawfully, fairly, and transparently.",
            domain="Legal"
        )
        
        # Create a task
        task_id = tag.create_task(
            name="Update GDPR compliance documentation",
            description="Review and update our GDPR compliance documentation for 2024",
            domain="Legal"
        )
        
        # Retrieve relevant knowledge
        relevant_chunks = tag.get_relevant_knowledge(task_id)
        
        print("Relevant knowledge chunks for the task:")
        for chunk in relevant_chunks:
            print(f"- {chunk['content']} (Distance: {chunk['distance']:.4f})")
            
    finally:
        tag.close()

if __name__ == "__main__":
    main() 