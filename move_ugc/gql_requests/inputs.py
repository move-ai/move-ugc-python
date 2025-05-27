"""Partials for input structures in the response."""


expand_clip_window = """
    clipWindow {
        startTime
        endTime
   }
"""


expand_progress = """
    progress{{
        state
        percentageComplete
    }}
"""

expand_inputs = f"""
   inputs {{
      {expand_clip_window}
      numberOfActors
      options {{
          floorPlane
          mocapModel
          trackBall
          trackFingers
          trackJerseyNumbers
      }}
   }}
"""
