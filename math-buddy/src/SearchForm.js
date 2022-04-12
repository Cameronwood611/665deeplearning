import { Form, Button, Upload, message, Card } from "antd";
import { InboxOutlined } from "@ant-design/icons";

const { Dragger } = Upload;

const finish = (values) => {
  console.log("In finish");
  fetch("upload", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(values),
  }).then((response) => console.log(response));
};

const props = {
  name: "file",
  customRequest: (stuff) => finish(stuff),
  // multiple: true,
  // // action: "https://www.mocky.io/v2/5cc8019d300000980a055e76",
  onChange(info) {
    const { status } = info.file;
    if (status !== "uploading") {
      console.log(info.file, info.fileList);
    }
    if (status === "done") {
      message.success(`${info.file.name} file uploaded successfully.`);
    } else if (status === "error") {
      message.error(`${info.file.name} file upload failed.`);
    }
  },
  // onDrop(e) {
  //   console.log("Dropped files", e.dataTransfer.files);
  // },
};

const SearchForm = () => {
  return (
    <Card>
      <Dragger {...props}>
        <p className="ant-upload-drag-icon">
          <InboxOutlined />
        </p>
        <p className="ant-upload-text">
          Click or drag file to this area to upload
        </p>
        <p className="ant-upload-hint">Support for a single or bulk upload.</p>
      </Dragger>
    </Card>
  );
};

export { SearchForm };
