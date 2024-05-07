def schedule_jobs(jobs):
    sorted_jobs = sorted(jobs, key=lambda j: j['deadline'])
    completion_time = 0
    total_lateness = 0

    for job in sorted_jobs:
        completion_time += job['processing_time']
        lateness = max(0, completion_time - job['deadline'])
        total_lateness += lateness

    return total_lateness

def main():
    jobs = []
    num_jobs = int(input("Enter the number of jobs: "))

    for i in range(1, num_jobs + 1):
        print(f"\nJob {i}:")
        processing_time = int(input("Enter processing time: "))
        deadline = int(input("Enter deadline: "))
        jobs.append({'id': i, 'processing_time': processing_time, 'deadline': deadline})

    total_lateness = schedule_jobs(jobs)

    print("\nScheduled Jobs:")
    for job in jobs:
        print(f"Job {job['id']}: Processing Time = {job['processing_time']}, Deadline = {job['deadline']}")

    print("\nTotal lateness:", total_lateness)

# Call the main function to start the program
if __name__ == "__main__":
    main()
