from saving_account import Saving_Account

wilma_saving = Saving_Account(100, 1.5)
wilma_saving.deposit(400)
wilma_saving.set_holder_name("Wilma")
print(wilma_saving.getbalance())
print(wilma_saving)