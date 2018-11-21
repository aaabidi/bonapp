require 'test_helper'

class HallsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @hall = halls(:one)
  end

  test "should get index" do
    get halls_url
    assert_response :success
  end

  test "should get new" do
    get new_hall_url
    assert_response :success
  end

  test "should create hall" do
    assert_difference('Hall.count') do
      post halls_url, params: { hall: { name: @hall.name } }
    end

    assert_redirected_to hall_url(Hall.last)
  end

  test "should show hall" do
    get hall_url(@hall)
    assert_response :success
  end

  test "should get edit" do
    get edit_hall_url(@hall)
    assert_response :success
  end

  test "should update hall" do
    patch hall_url(@hall), params: { hall: { name: @hall.name } }
    assert_redirected_to hall_url(@hall)
  end

  test "should destroy hall" do
    assert_difference('Hall.count', -1) do
      delete hall_url(@hall)
    end

    assert_redirected_to halls_url
  end
end
