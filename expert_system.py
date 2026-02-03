# ----------------------------------------
# Rule-Based Expert System using Forward Chaining
# ----------------------------------------

class ExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []
        self.inference_log = []

    def add_rule(self, conditions, conclusion):
        self.rules.append((set(conditions), conclusion))

    def add_fact(self, fact):
        self.facts.add(fact)

    def forward_chaining(self):
        applied = True
        while applied:
            applied = False
            for conditions, conclusion in self.rules:
                if conditions.issubset(self.facts) and conclusion not in self.facts:
                    self.facts.add(conclusion)
                    applied = True
                    self.inference_log.append(
                        f"IF {', '.join(conditions)} THEN {conclusion}"
                    )

    def show_results(self):
        print("\n--- INFERENCE LOG ---")
        for step in self.inference_log:
            print(step)

        print("\n--- FINAL FACTS / CONCLUSIONS ---")
        for fact in sorted(self.facts):
            print(fact)


# ----------------------------------------
# MAIN PROGRAM (DO NOT REMOVE THIS PART)
# ----------------------------------------
if __name__ == "__main__":

    print("=== Rule-Based Expert System ===")

    system = ExpertSystem()

    # RULE BASE
    system.add_rule(["fever", "cough"], "flu")
    system.add_rule(["flu", "body_pain"], "viral_infection")
    system.add_rule(["viral_infection"], "need_rest")
    system.add_rule(["headache", "stiff_neck"], "meningitis")
    system.add_rule(["meningitis"], "need_immediate_medical_attention")

    # USER INPUT
    print("\nEnter symptoms one by one.")
    print("Type 'done' to finish.\n")

    while True:
        symptom = input("Symptom: ").strip().lower()
        if symptom == "done":
            break
        if symptom:
            system.add_fact(symptom)

    # INFERENCE
    system.forward_chaining()

    # OUTPUT
    system.show_results()

