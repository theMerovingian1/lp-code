def max_profit_job_sequence(arr, t):
    n = len(arr)

    # Sort all jobs according to decreasing order of profit
    arr.sort(key=lambda x: x[2], reverse=True)

    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ['-1'] * t

    # Iterate through all given jobs
    for i in range(n):

        # Find a free slot for this job
        # (Note that we start from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    return job


def main():
    # Input jobs interactively
    arr = []
    while True:
        job = input("Enter job name (or 'done' to finish): ")
        if job.lower() == 'done':
            break
        deadline = int(input("Enter job deadline: "))
        profit = int(input("Enter job profit: "))
        arr.append((job, deadline, profit))

    # Input number of time slots
    t = int(input("Enter the number of time slots: "))

    # Get the maximum profit job sequence
    job_sequence = max_profit_job_sequence(arr, t)

    # Print the maximum profit job sequence
    print("Following is the maximum profit sequence of Jobs:")
    print(job_sequence)


if __name__ == "__main__":
    main()
