# OpenRouteService Response Notes

## Route response structure

response
└── routes (list)
    ├── [0] Route A
    │   ├── summary
    │   │   ├── duration (seconds)
    │   │   └── distance (meters)
    │   └── segments
    │       └── steps
    │           └── instruction
    └── [1] Route B

## Example output with one route

{
  "routes": [
    {
      "summary": {
        "distance": 1234.5,
        "duration": 1050.2
      },
      "segments": [
        {
          "distance": 1234.5,
          "duration": 1050.2,
          "steps": [
            {
              "instruction": "Head south",
              "distance": 100,
              "duration": 30
            }
          ]
        }
      ],
      "geometry": "encoded_polyline_here"
    }
  ],
  "bbox": [...],
  "metadata": {...}
}

## Useful fields for V1

duration:
route["summary"]["duration"]

distance:
route["summary"]["distance"]

Example:

Duration:
route["summary"]["duration"] / 60

Distance:
route["summary"]["distance"] / 1000