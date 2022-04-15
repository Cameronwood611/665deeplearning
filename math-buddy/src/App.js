import "./App.css";
import { Layout, Row, Col } from "antd";
import { SearchForm } from "./SearchForm";

const { Header, Content, Footer } = Layout;

function App() {
  return (
    <Layout>
      <Header className="header">
        <div className="logo" />
        <h1 style={{ color: "white" }}>Math Buddy</h1>
      </Header>
      <Content style={{ padding: "0 50px" }}>
        <Layout
          className="site-layout-background"
          style={{ padding: "24px 0" }}
        >
          <Content
            style={{ padding: "0 24px", minHeight: 280, height: "100%" }}
          >
            <Row>
              <Col xs={24} xl={6}></Col>
              <Col xs={24} xl={12}>
                <SearchForm />
              </Col>
              <Col xs={24} xl={8}></Col>
            </Row>
          </Content>
        </Layout>
      </Content>
      <Footer style={{ textAlign: "center" }}></Footer>
    </Layout>
  );
}

export default App;
