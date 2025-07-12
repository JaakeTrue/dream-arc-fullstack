import mongoose from 'mongoose';

const StudentSchema = new mongoose.Schema({
  name: String,
  grade: String,
  performance: Object,
  notes: Array
});

export default mongoose.model('Student', StudentSchema);
