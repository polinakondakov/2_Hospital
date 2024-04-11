from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base_meta import Base

class Appointment(Base):
    __tablename__ = "Appointment"  #Устанавливается имя таблицы в базе данных, соответствующее данному классу

    # Определяются столбцы в таблице
    doctor_id = Column(ForeignKey("Doctor.id"), primary_key=True)
    patient_id = Column(ForeignKey("Patient.id"), primary_key=True)
    office_number = Column(Integer, nullable=False)
    date_and_time = Column(String(20), nullable=False)

    # Устанавливаются связи
    doctor = relationship("Doctor", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")

    def __str__(self):
        return f"Service {self.office_number} {self.doctor_id} {self.patient_id} {self.date_and_time}"

    def __repr__(self):
        return str(self)