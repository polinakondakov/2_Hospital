from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base_meta import Base

class Doctor(Base):
    __tablename__ = "Doctor"  #Устанавливается имя таблицы в базе данных, соответствующее данному классу

    # Определяются столбцы в таблице
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    specialisation = Column(String(50), nullable=False)

    # Устанавливаются связи
    #patients = relationship("Patient", back_populates="doctor")
    services = relationship("Service", back_populates="doctor")
    appointments = relationship("Appointment", back_populates="doctor")

    def __str__(self):
        return f"Doctor {self.id} {self.full_name} {self.specialisation} "

    def __repr__(self):
        return str(self)