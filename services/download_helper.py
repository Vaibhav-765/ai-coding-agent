from io import BytesIO
import zipfile


def create_zip(modified_files):

    zip_buffer = BytesIO()

    with zipfile.ZipFile(
        zip_buffer,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:

        for file_name, code in modified_files.items():

            zip_file.writestr(
                file_name,
                code
            )

    zip_buffer.seek(0)

    return zip_buffer