import json

with open("reflection-tree.json") as f:
    data = json.load(f)

nodes = {node["id"]: node for node in data["nodes"]}

current = "START"
answers = {}

while True:
    node = nodes[current]
    
    print("\n" + node["text"])
    
    if node["type"] == "question":
        for i, opt in enumerate(node["options"], 1):
            print(f"{i}. {opt}")
        
        choice = int(input("Choose: ")) - 1
        selected = node["options"][choice]
        answers[current] = selected
        
        current = node["next"]
    
    elif node["type"] == "decision":
        rules = node["rules"].split(";")
        prev_answer = list(answers.values())[-1]
        
        for rule in rules:
            condition, target = rule.split(":")
            values = condition.split("=")[1].split("|")
            if prev_answer in values:
                current = target
                break
    
    else:
        if "next" in node:
            input("Press Enter to continue...")
            current = node["next"]
        else:
            break

print("\nSession Ended.")
