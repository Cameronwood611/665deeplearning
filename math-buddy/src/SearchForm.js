import { useState } from 'react';
import { Upload, message, Card } from "antd";
import { InboxOutlined } from "@ant-design/icons";

const { Dragger } = Upload;

const SearchForm = () => {
  const [link, setLink] = useState("");

  const props = {
    accept: ".png,.jpg,.jpeg",
    name: "file",
    action: "upload",
    onChange(info) {
      setLink("");
      const { status, response } = info.file;
      if (status === "done") {
        message.success(`${info.file.name} file uploaded successfully.`);
        console.log(response);
        setLink(response);
      } else if (status === "error") {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
    listType: "picture",
  };

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
      {link ? (
        <div style={{ display: 'flex' }}><iframe src={link} width="540" height="450" /></div>
      ) : null}
    </Card>
  );
};

export { SearchForm };
