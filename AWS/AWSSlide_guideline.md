# AWS Slide Guideline

Use this for every curriculum slide in `AWS/`.  
**Do not hand-edit** `AWS/AWSTraining.html` — edit sources, then:

```powershell
cd D:\Sangeetha\Python
python AWS/build_aws_training.py
```

---

## Source files

| File | Purpose |
|------|---------|
| `aws_catalog.py` | Skills W01–W16 (PDF §§25–34, 39) |
| `aws_assemble.py` | Builds meta / content / beginner / flows |
| `aws_flowcharts.py` | YES→right / NO→down |
| `build_aws_training.py` | Generator + SVG visual posters |

Shared: `interview_track.py`, `track_visual_guides.py`, `training_deck.py`.

**Do not claim deep Kubernetes** unless you actually operated a cluster. Map Pod ≈ ECS task if asked.

Cost questions: nine-step engineering sequence, not “just use Lambda.”
