## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
# yearly_salary = float(input("Enter yearly salary: "))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# cost_of_dream_home = float(input("Enter cost of your dream home: "))
# portion_down_payment = .25 # 25% of the cost of your dream home
# amount_saved = 0
# r = .05 # 5% yearly return on savings








# help gpt
yearly_salary = float(input("Enter yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter cost of your dream home: "))

portion_down_payment = 0.25  # 25% of the cost of your dream home
amount_saved = 0 # Inicializa o valor total economizado
r = 0.05  # 5% yearly return on savings

# Passo 1: Definir o valor necessário para o adiantamento
down_payment = cost_of_dream_home * portion_down_payment

# Passo 2: Inicializar o contador de meses   
months = 0   

# Loop que continua enquanto não houver economia suficiente para o adiantamento
while amount_saved < down_payment:
    # Calcula a economia mensal do salário
    monthly_savings = (yearly_salary / 12) * portion_saved
    
    # Atualiza o valor total economizado com a economia mensal e o retorno mensal
    amount_saved += monthly_savings + (amount_saved * r / 12)
    
    # Incrementa o contador de meses
    months += 1

# Imprime o número de meses necessários para atingir o adiantamento
print("Number of months:", months)



#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
