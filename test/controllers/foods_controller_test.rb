require 'test_helper'

class FoodsControllerTest < ActionDispatch::IntegrationTest
  test "should get name:string" do
    get foods_name:string_url
    assert_response :success
  end

  test "should get description:text" do
    get foods_description:text_url
    assert_response :success
  end

  test "should get has_many:comments" do
    get foods_has_many:comments_url
    assert_response :success
  end

  test "should get references:halls" do
    get foods_references:halls_url
    assert_response :success
  end

end
