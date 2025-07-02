style_code = """
<style>
  header, footer, [data-testid="stHeaderActionElements"], [data-testid="stMetricDelta"] svg {
    display: none !important;
  }

  [data-testid="stToastContainer"] {
    top: 1rem !important;
    right: 0.25rem !important;
  }

  body {
    -webkit-font-smoothing: antialiased;
  }

  [data-testid="stMainBlockContainer"]{
    padding: 1.25rem 1rem 2rem !important;
  }

  h1, h3 {
    font-weight: 500 !important;
    text-align: center !important;
  }

  h1 {
    font-size: 40px !important;
  }

  h3 {
    padding: 0 0 2.5rem !important;
    font-size: 24px !important;
  }

  [data-testid="stFileUploaderDropzone"], [data-testid="stCameraInputWebcamComponent"] {
    margin-top: 15px !important;
    padding: 2rem 1rem !important;
    border: 2px dashed #d3d2ca !important;
    border-radius: 1.2rem !important;
  }

  [data-testid="stFileUploaderDropzone"]{
    display: flex !important;
    flex-direction: column !important;
    gap: 2rem !important;
  }

  [data-testid="stFileUploaderDropzoneInstructions"]{
    margin: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    text-align: center !important;
    gap: 1rem !important;
  }

  @media (max-width: 767px) {
    [data-testid="stFileUploaderDropzoneInstructions"] {
      text-align: left !important;
      align-items: flex-start !important;
    }
  }

  [data-testid="stFileUploaderDropzoneInstructions"] span {
    margin: 0 !important;
  }
</style>
"""
