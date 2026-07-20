"""A program that prints mime type of input filename."""


def main():
    """Input filename and print its mime type."""
    filename = input("File name: ")
    mime_type = get_mime_type_from_filename(filename)
    print(mime_type)


def get_mime_type_from_filename(filename: str) -> str:
    """Returns corresponding mime type of given filename,
       using file extension at the end.

       Returns "application/octet-stream" if there is no
       mime type available."""
    extension = get_extension_from_filename(filename)
    mime_type = get_mime_type_from_extension(extension)

    if mime_type is None:
        # as per CS50 directions
        mime_type = "application/octet-stream"
    return mime_type


def get_extension_from_filename(filename: str) -> str | None:
    """Returns corresponding extension of a given filename.

    Returns None if there is no extension at all."""
    # rstrip: spaces on right side of filename cause parsing issues
    # as space is read litrally along with extension if not removed.
    if not filename:
        return None
    filename = filename.rstrip()

    if "." in filename:
        parts = filename.split(".")
    else:
        return None

    extension = parts[-1].lower()
    return extension


def get_mime_type_from_extension(extension: str | None) -> str | None:
    """Returns mime type for a given extension.

    Returns None if there is no corresponding mime type or if extension is None."""

    if not extension:
        return None

    mime_types = {
        # image/
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",

        # application/
        "pdf": "application/pdf",
        "zip": "application/zip",

        # text/
        "txt": "text/plain"
    }
    return mime_types.get(extension)


if __name__ == "__main__":
    main()
