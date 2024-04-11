from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from database.base_meta import Base

class Patient(Base):
    __tablename__ = "Patient"  #Устанавливается имя таблицы в базе данных, соответствующее данному классу

    # Определяются столбцы в таблице
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    phone_number = Column(Integer, nullable=False)
    sex = Column(String(10), nullable=False)
    bdate = Column(Date, nullable=True)

    # Устанавливаются связи
    #doctors = relationship("Doctor", back_populates="patient")
    appointments = relationship("Appointment", back_populates="patient")

    def __str__(self):
        return f"Patient {self.id} {self.full_name} {self.phone_number} {self.sex} {self.bdate} "

    def __repr__(self):
        return str(self)