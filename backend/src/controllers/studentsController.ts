import {{ Request, Response }} from 'express';
import Student from '../models/Student';

export const getStudent = async (req: Request, res: Response) => {
  try {
    const student = await Student.findById(req.params.id);
    res.json(student);
  } catch (error) {
    res.status(500).json({{ message: "Server error" }});
  }
};
