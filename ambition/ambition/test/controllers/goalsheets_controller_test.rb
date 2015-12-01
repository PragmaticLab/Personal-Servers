require 'test_helper'

class GoalsheetsControllerTest < ActionController::TestCase
  setup do
    @goalsheet = goalsheets(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:goalsheets)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create goalsheet" do
    assert_difference('Goalsheet.count') do
      post :create, goalsheet: { goals: @goalsheet.goals, time: @goalsheet.time }
    end

    assert_redirected_to goalsheet_path(assigns(:goalsheet))
  end

  test "should show goalsheet" do
    get :show, id: @goalsheet
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @goalsheet
    assert_response :success
  end

  test "should update goalsheet" do
    patch :update, id: @goalsheet, goalsheet: { goals: @goalsheet.goals, time: @goalsheet.time }
    assert_redirected_to goalsheet_path(assigns(:goalsheet))
  end

  test "should destroy goalsheet" do
    assert_difference('Goalsheet.count', -1) do
      delete :destroy, id: @goalsheet
    end

    assert_redirected_to goalsheets_path
  end
end
