class Parser:
    def __init__(self,table):
        self.table=table
        self.blank=""
        self.synch=""
    def parse(self,string):
        s1=string.split()
        s1.append("$")
        s2=string+"$"
        s2=s2.replace(" ","")
        matched,action,inputs,stack=[""],[""],[],[]
        inputs.append(s2)
        stack.append("E"+"$")  # starting symbol
        i=0
        j=s1[i]
        while stack[-1]!=inputs[-1]:
            if (j not in stack[-1] or j=="$") or (j==")" and j!=stack[-1][0]):
                if stack[-1][1]!="'":
                    if stack[-1][0] in self.table[j]:
                        if self.table[j][stack[-1][0]]!="synch":
                            action.append(f"{stack[-1][0]}->{self.table[j][stack[-1][0]]}")
                        else:
                            action.append(f"synch found!")
                            self.synch="synch"
                    else:
                        action.append(f"blank found!")
                        self.blank="blank"
                else:
                    if stack[-1][0:2] in self.table[j]:
                        if self.table[j][stack[-1][0:2]]!="synch":
                            action.append(f"{stack[-1][0]}{stack[-1][1]}->{self.table[j][stack[-1][0:2]]}")
                        else:
                            action.append(f"synch found!")
                            self.synch="synch"
                    else:
                        action.append(f"blank found!")
                        self.blank="blank"
                if self.blank!="blank":
                    if self.synch!="synch":
                        idx=stack[-1].find(stack[-1][0])
                        if stack[-1][1]!="'":
                            new_str=stack[-1][:idx]+stack[-1][idx+len(stack[-1][0]):]
                            if self.table[j][stack[-1][0]]!="ε":
                                stack.append(f"{self.table[j][stack[-1][0]]}{new_str}")
                            else:
                                stack.append(f"{new_str}")
                        else:
                            new_str=stack[-1][:idx] + stack[-1][idx+len(stack[-1][0:2]):]
                            if self.table[j][stack[-1][0:2]]!="ε":
                                stack.append(f"{self.table[j][stack[-1][0:2]]}{new_str}")
                            else:
                                stack.append(f"{new_str}")
                        matched.append(matched[-1])
                        inputs.append(inputs[-1])
                    else:
                        self.synch=""
                        idx=stack[-1].find(stack[-1][0])
                        if stack[-1][1]!="'":
                            new_str=stack[-1][:idx]+stack[-1][idx+len(stack[-1][0]):]
                            stack.append(f"{new_str}")
                        else:
                            new_str=stack[-1][:idx]+stack[-1][idx+len(stack[-1][0:2]):]
                            stack.append(f"{new_str}")
                        matched.append(matched[-1])
                        inputs.append(inputs[-1])
                else:
                    stack.append(stack[-1])
                    matched.append(matched[-1])
                    idx=inputs[-1].find(j)
                    new_str=inputs[-1][:idx]+inputs[-1][idx+len(j):]
                    inputs.append(new_str)
                    if j!="$":
                        i+=1
                        j=s1[i]
                    self.blank=""
            else:
                idx=inputs[-1].find(j)
                new_str=inputs[-1][:idx]+inputs[-1][idx+len(j):]
                idx_stack=inputs[-1].find(j)
                new_stack=stack[-1][:idx_stack]+stack[-1][idx_stack+len(j):]
                action.append(f"match {j}")
                stack.append(new_stack)
                matched.append(matched[-1]+j)
                inputs.append(new_str)
                if j!="$":
                    i+=1
                    j=s1[i]
        return matched,stack,inputs,action
def main():
    table = {
        "id": {"E": "TE'", "T": "FT'", "F": "id"},
        "+": {"E'": "+TE'", "T": "synch", "T'": "ε", "F": "synch"},
        "*": {"T'": "*FT'", "F": "synch"},
        "(": {"E": "TE'", "T": "FT'", "F": "(E)"},
        ")": {"E": "synch", "E'": "ε", "T": "synch", "T'": "ε", "F": "synch"},
        "$": {"E": "synch", "E'": "ε", "T": "synch", "T'": "ε", "F": "synch"}
    }  # parsing table given
    string= "id + id * id"  # input string
    parser = Parser(table)
    matched,stack,inputs,action = parser.parse(string)
    print("{:<25} {:<25} {:<25} {:<45}\n".format("MATCHED","STACK","INPUT","ACTION"))
    for matched_value, stack_value, inputs_value, action_value in zip(matched, stack, inputs, action):
        if action_value != "":
            print("{:<25} {:<25} {:<25} {:<45}\n".format(matched_value,stack_value,inputs_value,f"output {action_value}"))
        else:
            print("{:<25} {:<25} {:<25} {:<45}\n".format(matched_value,stack_value,inputs_value,f"{action_value}"))
if __name__ == "__main__":
    main()