import express from 'express';
const router = express.Router();

router.get('/:id', (req, res) => {
  res.json({
    id: req.params.id,
    name: "Sample Student", 
    grade: "A"
  });
});

export default router;
