class EmployeeEvaluationExpertSystem:
    def __init__(self):
        self.criteria = {
            "quality_of_work": ["Poor", "Fair", "Good", "Excellent"],
            "punctuality": ["Poor", "Fair", "Good", "Excellent"],
            "teamwork": ["Poor", "Fair", "Good", "Excellent"]
        }

    def evaluate_employee(self):
        print("Welcome to the Employee Evaluation Expert System")
        name = input("Enter employee's name: ")
        department = input("Enter employee's department: ")
        position = input("Enter employee's position: ")

        print("\nPlease rate the employee based on the following criteria (1 - Poor, 2 - Fair, 3 - Good, 4 - Excellent):")
        evaluation = {}
        for criterion, ratings in self.criteria.items():
            rating = int(input(f"{criterion.capitalize()}: "))
            evaluation[criterion] = ratings[rating - 1]

        print("\nEmployee Evaluation Report:")
        print(f"Name: {name}")
        print(f"Department: {department}")
        print(f"Position: {position}")
        print("\nCriteria Ratings:")
        for criterion, rating in evaluation.items():
            print(f"{criterion.capitalize()}: {rating}")

        # Provide recommendations based on evaluation
        self.provide_recommendations(evaluation)

    def provide_recommendations(self, evaluation):
        print("\nRecommendations:")
        if evaluation["quality_of_work"] == "Poor":
            print("- Provide additional training or resources to improve work quality.")
        if evaluation["punctuality"] == "Poor":
            print(
                "- Address any issues affecting punctuality and reinforce the importance of being on time.")
        if evaluation["teamwork"] == "Poor":
            print(
                "- Encourage collaboration and team-building activities to improve teamwork.")

        # Add more recommendations based on other criteria as needed


def main():
    expert_system = EmployeeEvaluationExpertSystem()
    expert_system.evaluate_employee()


if __name__ == "__main__":
    main()
