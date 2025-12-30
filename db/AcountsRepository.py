from models.Account import Account

class AccountsRepository:
    def __init__(self, db):
        self.db = db
    
    def add_account(self, account:Account):
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)

    def remove_account(self, account_id:str) -> bool:
        account = self.db.get_by_id(account_id)

        if not account:
            return False
        
        self.db.delete(account)
        self.db.commit()
        return True

    def get_accounts_by_user_id(self, user_id:str):
        return self.db.query(Account).filter(Account.user_id == user_id).all()

    def get_by_id(self, account_id:str) -> Account:
        return self.db.query(Account).filter(Account.account_id == account_id).first()

    def get_by_name(self, name:str) -> list[Account]:
        return self.db.query(Account).filter(Account.name == name).all()
    
    def update_remainig(self, account_id:str, type:str, amount:float) -> bool:
        account = self.get_by_id(account_id)

        if not account:
            return False
        
        if type == "deposit":           # Can implant with enum
            account.remaining += amount
            return True
        
        elif type == "withdraw":
            account.remaining -= amount
            return True
        